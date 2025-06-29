# 📚 Dio - Resumos

Repositório para armazenar resumos sobre o bootcamp **Santander 2025**.

---

## 📔 Documentação Oficial

- [📘 GitHub Docs](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
- [📙 Git Docs](https://git-scm.com/doc)

---

## 🧠 Resumos das Aulas

### 📑 Sumário

- [🌿 Trabalhando com Branches](#🌿-trabalhando-com-branches)
- [🧾 Convenções de Nomeação de Branches e Commits](#🧾-convenções-de-nomeação-de-branches-e-commits)

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