# 📚 Dio - Resumos

Repositório para armazenar resumos sobre o bootcamp **Santander 2025**.

---

## 📔 Documentação Oficial

- [📘 GitHub Docs](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
- [📙 Git Docs](https://git-scm.com/doc)

---

## 🧠 Resumos das Aulas

### 📑 Sumário

- [💾 Como Salvar Local e Remotamente com Git](#✅-etapas-para-salvar-localmente-e-remotamente-no-git)
- [🌿 Trabalhando com Branches](#🌿-trabalhando-com-branches)
- [🧾 Convenções de Nomeação de Branches e Commits](#🧾-convenções-de-nomeação-de-branches-e-commits)
- [💾 Salvando Alterações Temporariamente](#💾-salvando-alterações-temporariamente)
- [♻️ Restaurar Projeto para o último Commit](#️♻️-restaurar-projeto-para-o-último-commit)

---
### ✅ Etapas para salvar localmente e remotamente no Git

<details>
<summary><strong>Ver resumo completo</strong></summary>

#### Salvar localmente (commit)

Use os comandos abaixo para salvar suas alterações no seu repositório local:

```bash
git add .
git commit -m "mensagem explicando o que foi feito"
```

#### Enviar para o repositório remoto (push)

Após o commit, envie as alterações para o GitHub:

```bash
git push origin main
```

> Troque `main` pelo nome da sua branch, se for diferente.

---

### (Opcional) Conectar o repositório local ao GitHub

Se ainda não tiver conectado o repositório local a um remoto:

```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```

> Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelas suas informações do GitHub.

---

### Dica: Verificar o status antes de salvar

Você pode verificar o que foi alterado antes de salvar:

```bash
git status
```

---

## 🧠 Resumo

| Comando | Descrição |
|---------|-----------|
| `git add .` | Adiciona todas as alterações |
| `git commit -m "mensagem"` | Salva localmente |
| `git push origin main` | Envia para o GitHub |


</details>

---

### 🌿 Trabalhando com Branches

<details>
<summary><strong>Ver resumo completo</strong></summary>

#### 📌 Conceitos básicos

- Uma **branch** (ramo) é uma ramificação do seu projeto.
- Serve para trabalhar em diferentes versões ou funcionalidades **sem afetar diretamente o código principal**.
- Quando você cria uma nova branch, ela aponta para o **mesmo commit da branch atual**.
- As branches só se unem com o código principal quando são **mescladas (merge)**.

#### 🔧 Comandos importantes

| Comando | Descrição |
|--------|-----------|
| `git checkout -b nome-da-branch` | Cria e muda para uma nova branch |
| `git branch` | Lista todas as branches |
| `git branch -v` | Mostra as branches com os últimos commits |
| `git merge nome-da-branch` | Mescla a branch com a atual |
| `git branch -d nome-da-branch` | Exclui uma branch (depois de mesclada) |

---

#### ⚔️ Conflitos ao Mesclar

**Conflito de merge:** acontece quando duas pessoas alteram a **mesma linha** de um arquivo.  
É necessário escolher qual versão manter.

**Etapas para resolver:**

1. Escolher qual parte do código deve ficar.
2. Salvar o arquivo corrigido.
3. Executar os comandos abaixo:

```bash
git add .
git commit -m "resolve conflito"
git push origin main
```

🔁 Use `git pull` antes para garantir que tem a versão mais atual do repositório remoto.

</details>

---

### 🧾 Convenções de Nomeação de Branches e Commits

<details>
<summary><strong>Ver resumo completo</strong></summary>

#### 🌿 Nomeando Branches

Seguir padrões ajuda na organização e leitura por todos da equipe.

**Padrões comuns:**

| Prefixo | Uso |
|---------|-----|
| `feature/` | Nova funcionalidade ✨ |
| `fix/` | Correção de bug 🐛 |
| `hotfix/` | Correção urgente 🚑 |
| `release/` | Preparação para uma versão 📦 |
| `test/` | Testes ✅ |

**Exemplos:**
- `feature/cadastro-usuario`
- `fix/navbar-responsiva`

---

#### 📝 Mensagens de Commit (Conventional Commits)

Padrão para manter um histórico limpo e fácil de entender.

| Tipo | Uso |
|------|-----|
| `feat:` | Nova funcionalidade ✨ |
| `fix:` | Correção de bug 🐛 |
| `docs:` | Documentação 📚 |
| `style:` | Alteração visual ou de formatação 💅 |
| `refactor:` | Refatoração (melhoria sem mudar comportamento) 🧹 |
| `test:` | Testes adicionados ou modificados 🧪 |
| `chore:` | Manutenções gerais 🔧 |

**Exemplos:**
- `feat: adiciona página de login`
- `fix: corrige erro na validação do email`

🎯 **Objetivo:** facilitar a colaboração, leitura do histórico e rastreabilidade de problemas.

</details>

---

### 💾 Salvando Alterações Temporariamente

<details>
<summary><strong>Ver resumo completo</strong></summary>

#### 📦 Backup com commit temporário

Se quiser salvar as alterações antes de restaurar ou testar algo:

| tipo | uso |
|------|-----|
| git add . | Adiciona a area de trabalho |
| git commit -m "Backup temporário antes de restaurar" | salva no git |
| git reset HEAD~1 | 🧼 Depois, para desfazer esse commit (se quiser): |

</details>

---

### ♻️ Restaurar Projeto para o último Commit

<details>
<summary><strong>Ver resumo completo</strong></summary>

#### 🔄 Descartar alterações e voltar ao último commit

Se você quiser desfazer todas as modificações e restaurar o repositório para o estado do último commit:

| tipo | uso |
|------|-----|
| git restore . | Restaura todos os arquivos modificados. |
| git clean -fd | Remove arquivos e pastas não rastreados. |

#### 👀 Verificar antes de remover arquivos não rastreados
```
 git clean -nfd
```
O -n (ou --dry-run) simula a exclusão, mostrando o que será removido sem apagar nada ainda.


</details>


