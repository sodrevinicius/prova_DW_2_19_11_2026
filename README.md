# Prova Prática Individual — Desenvolvimento Web II — Versão B

**Fatec Porto Ferreira · CST em Desenvolvimento de Software Multiplataforma**
**Quinta-feira, 19/11/2026 · 19h30 às 22h00 · Prof. Vagner dos Santos**

Este repositório contém um sistema de **salas** que **já executa**, mas está incompleto e tem duas falhas. A prova consiste em resolver os itens numerados abaixo.

---

## Regras

1. A prova é **individual**.
2. **Consulta permitida** ao material da disciplina: apostilas, Anexos de Python e projetos-exemplo das aulas.
3. **É proibido o uso de inteligência artificial** — assistentes de conversa, extensões de autocompletar do editor ou qualquer ferramenta que gere código ou texto — e a comunicação com colegas durante a prova.
4. Havendo indício de descumprimento da regra 3, **a nota fica suspensa** e você receberá uma devolutiva considerando o que foi observado.
5. A entrega é feita **somente pelo GitHub**. Vale o que estiver no seu repositório, enviado com `git push`, **até as 22h00** (ou até o horário individual informado pelo professor). O que não foi enviado não será corrigido.
6. **Não altere** nomes de arquivos, endereços de rotas, nomes de campos nem a função `preparar_banco`. **Não instale pacotes** além dos que estão no `requirements.txt`.

---

## Como executar

Na raiz do projeto, com o ambiente virtual ativo:

```
pip install -r requirements.txt
python app.py
```

Conta inicial para entrar no sistema:

```
e-mail: coordenacao@fatec.local
senha:  prova123
```

Para recomeçar com o banco original, pare o servidor e apague a pasta `instance`.

---

## Como entregar

Ao terminar **cada item**, grave e envie:

```
git add .
git commit -m "item 4"
git push
```

Use exatamente a mensagem `item N`, com o número do item. Para o arquivo de respostas, use a mensagem `respostas`. **Envie a cada item** — não deixe para o final.

---

## Estrutura do projeto

```
app.py                              # cria o app e a conta inicial
models/sala.py                  # entidade Sala
models/usuario.py
dao/sala_dao.py                 # acesso aos dados de Sala
dao/usuario_dao.py
controllers/sala_controller.py  # paginas
controllers/auth_controller.py      # entrar, criar conta e sair
controllers/api_controller.py       # dados em JSON
templates/                          # base, index, editar, login, cadastro
static/script.js
RESPOSTAS.md                        # voce escreve as respostas R1 e R2 aqui
```

---

## Itens

Todos os itens têm o **mesmo valor** e são **independentes**: se travar em um, passe ao seguinte. Os itens 2, 3, 4, 5, 7, 8 e 9 estão marcados no código com um comentário `ITEM N`. Os itens 1 e 6 são **falhas**: o enunciado descreve o sintoma e o arquivo, e você encontra a causa.

### Item 1 — Falha no cadastro · `dao/sala_dao.py`

**Sintoma:** ao cadastrar pela tela, a mensagem de sucesso aparece, mas o registro **não fica gravado**: ele não aparece na lista.

**Está pronto quando:** um registro cadastrado pela tela aparece na lista e continua lá depois de parar e iniciar o servidor.

> Ao terminar, `git commit -m "item 1"` e `git push`.

### Item 2 — Contagem e lista vazia · `templates/index.html`

Acima da lista, exiba:

- havendo registros, a contagem, no formato `N registro(s).` — por exemplo, `3 registro(s).`;
- não havendo nenhum, a frase `Nenhuma sala cadastrada.`

**Está pronto quando:** com registros aparece só a contagem; depois de excluir todos, aparece só a frase.

> Ao terminar, `git commit -m "item 2"` e `git push`.

### Item 3 — Contador na sessão · `controllers/sala_controller.py`

Conte, **na sessão**, quantas vezes a pessoa abriu a listagem. A chave da sessão deve se chamar `acessos`. O template já exibe o valor, no rodapé da página.

**Está pronto quando:** o número ao lado de "Acessos nesta sessão" aumenta de 1 em 1 a cada vez que a listagem é aberta.

> Ao terminar, `git commit -m "item 3"` e `git push`.

### Item 4 — Gravar a edição · `controllers/sala_controller.py`

O formulário de edição abre preenchido e é enviado por `POST`, mas nada é gravado. Trate o envio na rota `editar`: grave a alteração e redirecione para a listagem.

**Está pronto quando:** depois de editar e salvar, a listagem mostra os valores novos.

> Ao terminar, `git commit -m "item 4"` e `git push`.

### Item 5 — Proteção das páginas · `controllers/sala_controller.py`

Hoje qualquer pessoa abre a listagem e a edição sem entrar no sistema. Proteja **todas** as rotas desse Blueprint em **um ponto só**: quem não estiver logado deve ser redirecionado para a tela de entrada.

**Está pronto quando:** sem entrar no sistema, abrir `/` ou `/editar/1` leva à tela de entrada; depois de entrar, as páginas abrem normalmente.

> Ao terminar, `git commit -m "item 5"` e `git push`.

### Item 6 — Falha no cadastro de conta · `controllers/auth_controller.py`

**Sintoma:** uma conta criada pela tela "Criar conta" **não consegue entrar** no sistema, embora a conta inicial entre normalmente. Além disso, a senha dessa conta fica **legível** no banco de dados.

**Está pronto quando:** uma conta nova, criada depois da correção, consegue entrar. (Contas criadas antes da correção continuam sem entrar: crie outra, com outro e-mail, para testar.)

> Ao terminar, `git commit -m "item 6"` e `git push`.

### Item 7 — Ler um registro pela API · `controllers/api_controller.py`

Crie a rota `GET /api/salas/<id>`, que devolve **um** registro em JSON. Se o id não existir, a resposta é **404**, com o corpo `{"erro": "Sala nao encontrada."}`.

**Está pronto quando:** logado, abrir `/api/salas/1` mostra o JSON do registro, e `/api/salas/999` responde 404 com o JSON de erro.

> Ao terminar, `git commit -m "item 7"` e `git push`.

### Item 8 — Atualizar a lista sem recarregar · `static/script.js`

Ao clicar em "atualizar lista", a página deve pedir a lista à API, no endereço `/api/salas`, e redesenhá-la com o que chegar, **sem recarregar**. Use as funções que já existem no arquivo. Se não for possível falar com o servidor, avise na tela.

**Está pronto quando:** ao clicar no botão, a lista é redesenhada e aparece o aviso "… registro(s) lido(s) sem recarregar a página."

> Ao terminar, `git commit -m "item 8"` e `git push`.

### Item 9 — Remover um registro pela API · `controllers/api_controller.py`

Crie a rota `DELETE /api/salas/<id>`, que remove **um** registro. Em caso de sucesso, a resposta é **204**, sem corpo. Se o id não existir, **404**, com o corpo `{"erro": "Sala nao encontrada."}`.

Para testar, entre no sistema, abra o console do navegador **na aba do sistema** e execute:

```javascript
fetch("/api/salas/1", { method: "DELETE" })
  .then(function (r) { console.log(r.status); });
```

**Está pronto quando:** o console mostra 204 e o registro some da listagem; repetir o mesmo comando mostra 404.

> Ao terminar, `git commit -m "item 9"` e `git push`.

### Item 10 — Resposta R1 · `RESPOSTAS.md`

Em uma **janela anônima** (sem entrar no sistema), com o **painel de rede** aberto, abra **dois** endereços e anote o código de status de cada um:

- **(a)** a página inicial do sistema: `/`
- **(b)** o endereço da API: `/api/salas` — digite-o **por inteiro** na barra de endereços

Em `RESPOSTAS.md`, registre os **dois** códigos e explique, em uma ou duas frases suas, **por que eles são diferentes**.

> Ao terminar, `git commit -m "item 10"` e `git push`.

### Item 11 — Resposta R2 · `RESPOSTAS.md`

**Depois de entrar no sistema**, abra o console do navegador **na aba do sistema** e execute:

```javascript
fetch("/api/sala")
  .then(function (r) { console.log(r.status); });
```

No arquivo `RESPOSTAS.md`, registre o **código de status** que apareceu e explique, em uma ou duas frases suas, o que ele significa neste caso.

> Ao terminar, `git commit -m "item 11"` e `git push`.

### Item 12 — Uso do Git

Cada item resolvido tem o **seu próprio** commit, com a mensagem `item N`, enviado ao GitHub durante a prova.

Resolver dois itens e gravar os dois em um commit só **não** atende: o histórico precisa mostrar a sequência do seu trabalho. Se um item for resolvido de passagem junto com outro, cite os dois números na mensagem (`item 3 e 5`).

---

## Como a prova é corrigida

Cada um dos 12 itens é avaliado como **atende** ou **não atende**, pelo critério "está pronto quando". Não há meio ponto por item.

**Nota = (itens atendidos ÷ 12) × 10**

Boa prova.
