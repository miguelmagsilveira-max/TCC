# Guia de Estudo — Nicholas

### 🎤 Sua parte: **Funcionalidades de gestão, alertas e relatórios**

Você mostra o que o sistema **faz na prática** — a "mágica" do dia a dia: o ciclo de vida de um equipamento, os alertas automáticos e os relatórios. É a parte que mais mostra **valor** para a empresa.

---

## 1. Sua parte em uma frase

> "O Stock Flow acompanha cada equipamento do cadastro até a baixa, avisa sozinho quando o estoque está baixo ou a garantia vai vencer, e gera relatórios em PDF com uma análise inteligente do inventário."

---

## 2. Explicação de verdade (para você entender)

### O ciclo de vida de um ativo (a espinha dorsal)
Um equipamento passa por **situações**, e o sistema controla cada mudança:

```
Cadastro → Em estoque → (Vincular) → Em uso → (Devolver) → Em estoque
                              ↓                        ↑
                         Manutenção ───(Retornar)─────┘
                              ↓
                         Desativado (baixa)
```

- **Em estoque**: cadastrado e disponível.
- **Em uso**: emprestado a um colaborador (vinculado).
- **Manutenção**: enviado para reparo.
- **Desativado**: deu baixa (não conta mais no inventário, mas o histórico fica).

Cada uma dessas ações gera um **registro no histórico** — quem fez, quando e o quê. Uma regra importante: **um equipamento em manutenção não pode ser emprestado** (faz sentido: está quebrado).

### Alertas automáticos (o sistema "avisa" sozinho)
O sistema monitora e gera dois tipos de alerta:
1. **Estoque baixo**: cada tipo de ativo tem um **mínimo** configurado. Se o estoque cai abaixo disso (ex.: mínimo 2 notebooks, só tem 1), o sistema alerta para repor.
2. **Garantia vencendo**: se a garantia de um equipamento vence nos **próximos 30 dias**, ele avisa — dá tempo de acionar o fornecedor.

### Relatórios em PDF + a **Curva ABC**
O sistema gera um **relatório em PDF** com a lista de ativos, pronto para imprimir ou enviar. Além disso, faz uma análise chamada **Curva ABC**:
- **Classe A**: os poucos itens que representam a **maior parte do valor** (até 80% do total). Merecem mais atenção.
- **Classe B**: itens de valor intermediário (até 95%).
- **Classe C**: a maioria dos itens, mas de **menor valor** somado.

> Analogia: numa casa, a **Classe A** é a TV e o notebook (poucos, mas caros); a **Classe C** são os cabos e adaptadores (muitos, mas baratos). A Curva ABC ajuda o gestor a focar no que é mais caro/importante. É um conceito clássico de administração de estoques.

---

## 3. Por que fizemos assim (decisões que impressionam)

- **Por que registrar tudo no histórico?** Para dar **rastreabilidade**: a qualquer momento se sabe toda a "vida" do equipamento.
- **Por que alertas automáticos?** Para o gestor **agir antes do problema** (repor antes de faltar, renovar garantia antes de vencer) — o sistema é proativo.
- **Por que a Curva ABC?** Porque nem todo item merece o mesmo esforço de gestão. Ela ajuda a **priorizar o que tem mais valor** — mostra que o projeto pensa como uma ferramenta de gestão real, não só um cadastro.
- **Por que PDF?** É um formato universal, fácil de arquivar, imprimir e compartilhar.

---

## 4. Glossário (fale com naturalidade)

| Termo | Tradução simples |
|-------|------------------|
| **Ativo** | Um equipamento de TI (notebook, monitor...). |
| **Vincular** | Emprestar/atribuir um ativo a um colaborador. |
| **Situação** | O estado atual do ativo (em estoque, em uso, manutenção, desativado). |
| **Ciclo de vida** | Todas as fases pelas quais o ativo passa. |
| **Estoque mínimo** | A quantidade mínima antes de disparar alerta de reposição. |
| **Curva ABC** | Análise que classifica itens por relevância de valor (A, B, C). |
| **Inventário** | A lista de todos os ativos ativos da empresa. |

---

## 5. Roteiro de fala (ensaie ~2 min)

> "Agora, o que o sistema faz na prática. Tudo gira em torno do **ciclo de vida do ativo**. Um equipamento entra como **'em estoque'**; quando é emprestado a alguém, vira **'em uso'**; se quebra, vai pra **'manutenção'**; e no fim da vida útil, é **desativado**. Cada uma dessas mudanças fica registrada no histórico — com data e responsável.
>
> Além disso, o sistema **avisa sozinho** em duas situações: quando o **estoque de um tipo fica abaixo do mínimo**, e quando uma **garantia está para vencer nos próximos 30 dias**. Isso deixa o gestor um passo à frente.
>
> E, para fechar, o sistema gera **relatórios em PDF** e faz a **Curva ABC**, uma análise que separa os itens pelo valor: a classe A são os poucos itens mais caros, que merecem mais controle, e a classe C são os muitos itens baratos. É como numa casa: a TV é classe A, os cabos são classe C. Com isso, o Stock Flow vira uma ferramenta real de gestão. Agora o Gustavo vai mostrar a parte visual do sistema."

---

## 6. Perguntas que a banca pode fazer

**"Um equipamento em manutenção pode ser emprestado?"**
→ "Não. O sistema impede isso — primeiro ele precisa retornar da manutenção para o estoque."

**"Como funciona o alerta de estoque?"**
→ "Cada tipo de ativo tem um mínimo configurado. Se a quantidade em estoque fica abaixo, o sistema gera um alerta de reposição."

**"O que é a Curva ABC e para que serve?"**
→ "É uma classificação por valor: classe A são poucos itens que somam a maior parte do valor; C são muitos itens de baixo valor. Serve para o gestor priorizar o controle dos itens mais importantes."

**"O que acontece quando um ativo é desativado?"**
→ "Ele sai do inventário ativo, mas não é apagado — o histórico dele é preservado para consulta."

---

## 7. Onde isso está no projeto

- [app/routers/ativos.py](../../app/routers/ativos.py) — cadastro, vinculação, manutenção, desativação (o ciclo de vida).
- [app/routers/alertas.py](../../app/routers/alertas.py) — a lógica dos alertas de estoque e garantia.
- [app/routers/relatorios.py](../../app/routers/relatorios.py) — geração do PDF e cálculo da Curva ABC.
- [docs/4-casos-de-uso.md](../4-casos-de-uso.md) — todos os casos de uso do sistema.
</content>
