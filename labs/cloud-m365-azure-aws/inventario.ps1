$ErrorActionPreference = 'Stop'
$dados = Get-Content -Raw (Join-Path $PSScriptRoot 'inventario.json') | ConvertFrom-Json
$usuarios = @($dados.usuarios)
if ($usuarios.Count -ne 2) { throw 'Inventario de teste inesperado' }
$usuarios | Group-Object licenca | Select-Object Name, Count
$semMfa = @($usuarios | Where-Object { $_.mfa -ne $true })
if ($semMfa.Count -ne 1) { throw 'Contagem MFA inesperada' }
Write-Output 'Inventario ficticio validado'
