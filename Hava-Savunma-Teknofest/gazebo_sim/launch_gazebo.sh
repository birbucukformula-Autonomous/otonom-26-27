#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export IGN_GAZEBO_RESOURCE_PATH="${SCRIPT_DIR}/models:${IGN_GAZEBO_RESOURCE_PATH:-}"

ign gazebo "${SCRIPT_DIR}/world.sdf"
