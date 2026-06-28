from __future__ import annotations

from typing import Any


ROLE_LABELS = {
    "component_additive": "additive",
    "component_aryl_halide": "aryl-halide",
    "component_base": "base",
    "component_ligand": "ligand",
    "component_substrate": "substrate",
    "component_electrophile": "electrophile",
}


def component_role_label(group_column: str | None) -> str | None:
    if not group_column:
        return None
    return ROLE_LABELS.get(group_column, group_column.replace("component_", "").replace("_", "-"))


def split_display_name(split_name: str, split_payload: dict[str, Any] | None = None) -> str:
    split_payload = split_payload or {}
    group_column = split_payload.get("group_column")
    role = component_role_label(group_column)
    if split_name == "grouped_high_cardinality_component" and role:
        return f"{role}-held-out grouped split"
    if split_name.startswith("out_of_") and role:
        return f"{role}-held-out split"
    return split_name.replace("_", " ")


def equivalent_grouped_split_note(primary_split: str, splits: dict[str, dict[str, Any]]) -> str | None:
    primary = splits.get(primary_split, {})
    group_column = primary.get("group_column")
    if not group_column:
        return None
    equivalent = [
        name
        for name, payload in splits.items()
        if name != primary_split and payload.get("is_valid") and payload.get("group_column") == group_column
    ]
    if not equivalent:
        return None
    role = component_role_label(group_column) or group_column
    return (
        f"In this dataset, {primary_split} uses {group_column}; it is therefore the "
        f"{role}-held-out grouped split and shares the same held-out group design as "
        f"{', '.join(equivalent)}."
    )
