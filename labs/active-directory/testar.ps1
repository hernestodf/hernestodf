$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'validar.ps1')
function Test-Rejeicao($dados) {
    $rejeitado = $false
    try { Test-Inventario $dados } catch { $rejeitado = $true }
    if (-not $rejeitado) { throw 'Entrada invalida aceita' }
}
Test-Rejeicao @{ous=@('TI');usuarios=@(@{login='ana.demo';ou='TI'},@{login='ana.demo';ou='TI'})}
Test-Rejeicao @{ous=@('TI');usuarios=@(@{login='ana.demo';ou='Outra'})}
Test-Rejeicao @{ous=@('TI');usuarios=@()}
Write-Output 'Testes aprovados'
