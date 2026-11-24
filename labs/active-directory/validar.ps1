param([string]$Arquivo = (Join-Path $PSScriptRoot 'inventario.json'))
$ErrorActionPreference = 'Stop'
function Test-Inventario($Dados) {
    $nomes = @{}
    foreach ($u in $Dados.usuarios) {
        if ($u.login -notmatch '^[a-z][a-z0-9.]{2,19}$') { throw 'Login invalido' }
        if ($nomes.ContainsKey($u.login)) { throw 'Login duplicado' }
        if ($u.ou -notin $Dados.ous) { throw 'OU inexistente' }
        $nomes[$u.login] = $true
    }
    if (@($Dados.usuarios).Count -eq 0) { throw 'Inventario vazio' }
}
Test-Inventario (Get-Content -Raw $Arquivo | ConvertFrom-Json)
Write-Output 'Inventario ficticio validado'
