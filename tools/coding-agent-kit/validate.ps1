[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Push-Location $root
try {
    & python 'tools/coding-agent-kit/validate.py'
    exit $LASTEXITCODE
}
finally {
    Pop-Location
}
