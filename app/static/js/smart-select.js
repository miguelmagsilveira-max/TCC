class SmartSelect {
  constructor({ container, contexto, inputName, placeholder = 'Selecione...', valor = '' }) {
    this.el = typeof container === 'string' ? document.querySelector(container) : container;
    this.contexto = contexto;
    this.inputName = inputName;
    this.placeholder = placeholder;
    this.valor = valor;
    this.opcoes = [];
    this.open = false;

    this._render();
    this._bind();
    this._fetch();
  }

  _render() {
    this.el.innerHTML = `
      <div class="ss-root relative">
        <input type="hidden" name="${this.inputName}" value="${this._esc(this.valor)}">
        <button type="button" class="ss-trigger w-full px-3 py-2.5 border border-slate-300 rounded-lg text-sm text-left flex items-center justify-between bg-white focus:outline-none focus:ring-2 focus:ring-blue-500">
          <span class="ss-display ${this.valor ? 'text-slate-800' : 'text-slate-400'}">${this._esc(this.valor || this.placeholder)}</span>
          <svg class="ss-chevron w-4 h-4 text-slate-400 flex-shrink-0 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
          </svg>
        </button>
        <div class="ss-dropdown hidden absolute z-50 w-full mt-1 bg-white border border-slate-200 rounded-lg shadow-lg">
          <div class="p-2 border-b border-slate-100">
            <input type="text" class="ss-search w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Buscar ou digitar novo...">
          </div>
          <ul class="ss-list max-h-48 overflow-y-auto p-2 space-y-0.5"></ul>
          <div class="ss-add hidden p-2 border-t border-slate-100">
            <button type="button" class="ss-add-btn w-full px-3 py-2 text-sm text-blue-600 hover:bg-blue-50 rounded-md text-left flex items-center gap-2 transition-colors">
              <svg class="w-4 h-4 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/>
              </svg>
              <span class="ss-add-label"></span>
            </button>
          </div>
        </div>
      </div>`;

    const r = this.el.querySelector('.ss-root');
    this.hidden   = r.querySelector('input[type="hidden"]');
    this.trigger  = r.querySelector('.ss-trigger');
    this.display  = r.querySelector('.ss-display');
    this.chevron  = r.querySelector('.ss-chevron');
    this.dropdown = r.querySelector('.ss-dropdown');
    this.search   = r.querySelector('.ss-search');
    this.list     = r.querySelector('.ss-list');
    this.addWrap  = r.querySelector('.ss-add');
    this.addBtn   = r.querySelector('.ss-add-btn');
    this.addLabel = r.querySelector('.ss-add-label');
    this.root     = r;
  }

  _bind() {
    this.trigger.addEventListener('click', () => this._toggle());

    this.search.addEventListener('input', () => this._renderList(this.search.value));

    this.list.addEventListener('click', async e => {
      // Clique no botão de excluir opção
      const delBtn = e.target.closest('[data-delete-id]');
      if (delBtn) {
        e.stopPropagation();
        const id = parseInt(delBtn.dataset.deleteId);
        const opcao = this.opcoes.find(o => o.id === id);
        await this._deleteOpcao(id);
        if (opcao && this.valor === opcao.valor) this._clear();
        this._renderList(this.search.value);
        return;
      }

      // Clique no botão de selecionar opção
      const btn = e.target.closest('[data-valor]');
      if (btn) this._select(btn.dataset.valor);
    });

    this.addBtn.addEventListener('click', async () => {
      const v = this.search.value.trim();
      if (v) { await this._addNew(v); this._select(v); }
    });

    this.search.addEventListener('keydown', e => {
      if (e.key === 'Enter') {
        e.preventDefault();
        const first = this.list.querySelector('[data-valor]');
        if (first) { this._select(first.dataset.valor); }
        else if (this.search.value.trim()) { this.addBtn.click(); }
      } else if (e.key === 'Escape') {
        this._close();
      }
    });

    document.addEventListener('click', e => {
      if (!this.root.contains(e.target)) this._close();
    });
  }

  async _fetch() {
    try {
      const res = await fetch(`/api/opcoes/${this.contexto}`);
      if (!res.ok) throw new Error('fetch failed');
      this.opcoes = await res.json();
      // Re-renderiza se o dropdown já estiver aberto quando a resposta chegar
      if (this.open) this._renderList(this.search.value);
    } catch (_) {
      this.opcoes = [];
    }
  }

  _renderList(filter = '') {
    const q = filter.toLowerCase();
    const filtered = q ? this.opcoes.filter(o => o.valor.toLowerCase().includes(q)) : this.opcoes;

    // Ícone lixeira — aparece apenas DENTRO do dropdown, ao lado de cada opção
    const trashSvg = `<svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
    </svg>`;

    const checkSvg = `<svg class="w-3.5 h-3.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
    </svg>`;

    this.list.innerHTML = filtered.map(o => {
      const active = this.valor === o.valor;
      return `
        <li class="flex items-center gap-0.5 group/item">
          <button type="button" data-valor="${this._esc(o.valor)}"
            class="flex-1 min-w-0 px-3 py-2 text-sm text-left rounded-md flex items-center gap-2 transition-colors
                   ${active ? 'text-blue-600 font-medium bg-blue-50' : 'text-slate-700 hover:bg-slate-100'}">
            ${active ? checkSvg : ''}
            <span class="truncate">${this._esc(o.valor)}</span>
          </button>
          <button type="button" data-delete-id="${o.id}"
            class="opacity-0 group-hover/item:opacity-100 p-1.5 rounded text-slate-400 hover:text-red-500 transition-all flex-shrink-0"
            title="Remover opção">
            ${trashSvg}
          </button>
        </li>`;
    }).join('');

    const trimmed = filter.trim();
    const exists = this.opcoes.some(o => o.valor.toLowerCase() === trimmed.toLowerCase());
    if (trimmed && !exists) {
      this.addLabel.textContent = `Adicionar "${trimmed}"`;
      this.addWrap.classList.remove('hidden');
    } else {
      this.addWrap.classList.add('hidden');
    }
  }

  _toggle() { this.open ? this._close() : this._open(); }

  _open() {
    this.open = true;
    this.dropdown.classList.remove('hidden');
    this.chevron.style.transform = 'rotate(180deg)';
    this.search.value = '';
    this._renderList();
    setTimeout(() => this.search.focus(), 0);
  }

  _close() {
    this.open = false;
    this.dropdown.classList.add('hidden');
    this.chevron.style.transform = '';
  }

  _select(valor) {
    this.valor = valor;
    this.hidden.value = valor;
    // Atualiza APENAS o texto do campo — nenhum ícone aqui
    this.display.textContent = valor;
    this.display.classList.remove('text-slate-400');
    this.display.classList.add('text-slate-800');
    this._close();
  }

  _clear() {
    this.valor = '';
    this.hidden.value = '';
    this.display.textContent = this.placeholder;
    this.display.classList.remove('text-slate-800');
    this.display.classList.add('text-slate-400');
  }

  async _addNew(valor) {
    try {
      const res = await fetch(`/api/opcoes/${this.contexto}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ valor }),
      });
      if (res.ok) {
        const nova = await res.json();
        if (!this.opcoes.some(o => o.valor === nova.valor)) {
          this.opcoes.push(nova);
          this.opcoes.sort((a, b) => a.valor.localeCompare(b.valor));
        }
      }
    } catch (_) {}
  }

  async _deleteOpcao(id) {
    try {
      await fetch(`/api/opcoes/${this.contexto}/${id}`, { method: 'DELETE' });
      this.opcoes = this.opcoes.filter(o => o.id !== id);
    } catch (_) {}
  }

  _esc(str) {
    return String(str ?? '').replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  static initAll() {
    document.querySelectorAll('[data-smart-select]').forEach(el => {
      new SmartSelect({
        container: el,
        contexto:    el.dataset.contexto,
        inputName:   el.dataset.name,
        placeholder: el.dataset.placeholder || 'Selecione...',
        valor:       el.dataset.valor || '',
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', () => SmartSelect.initAll());
