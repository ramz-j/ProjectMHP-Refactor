# CHANGELOG

Este archivo documenta los cambios realizados al framework original ProjectMHP con fines de reingeniería, para mejorar su modularidad, mantenibilidad y organización.

## [Estructura-Modular] - 2025-06-22
### Cambios principales
- Reorganizadas carpetas: `algorithms`, `problems`, `agent`, `state`, `stats`, `operators`, `utils`.
- Renombrados archivos siguiendo la convención `snake_case`.
- Actualizadas todas las importaciones afectadas.

### Reestructuración de la carpeta DATA
- Renombrada la carpeta `DATA/` a `experiments/`, reorganizada en subcarpetas:
  - `algorithms_config/` (antes `config/`)
  - `problems_instances/` (antes `instances/`)
  - `results/` (antes `output/`)
  - `analysis/` (antes `matlab/`)
- Carpetas internas de `algorithms_config/` y `problems_instances/` renombradas a minúsculas (ej: `GA` → `ga`, `TSP` → `tsp`).
- Rutas internas del código actualizadas para reflejar estos cambios.

## [Original] - (versión del profesor)
- Versión original del framework clonada desde el repositorio del profesor.

