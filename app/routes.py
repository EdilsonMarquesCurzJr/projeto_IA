from flask import Flask, render_template
from forms import CadastroForm
import os

app = Flask(__name__)

template_dir = os.path.abspath('./tem')
app.template_folder = template_dir

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historico')
def historico():
    return render_template('historico.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    form = CadastroForm()

    if form.validate_on_submit():
        data = {
            'nome': form.nome.data,
            'loa': form.loa.data,
            'boca': form.boca.data,
            'dwt': form.dwt.data,
            'calado_entrada': form.calado_entrada.data,
            'calado_saida': form.calado_saida.data,
            'calado_aereo': form.calado_aereo.data,
            'pontal': form.pontal.data,
            'tamanho_lanca': form.tamanho_lanca.data,
            'ano_construcao': form.ano_construcao.data,
            'tipo_navio': form.tipo_navio.data,
            'ultimo_porto': form.ultimo_porto.data,
            'proximo_porto': form.proximo_porto.data,
            'data_chegada': form.data_chegada.data,
        }
        # Realize ações com os dados, como salvá-los em um banco de dados
        print(data)

    return render_template('cadastro.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
