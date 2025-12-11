from flask import Flask, render_template_string, request, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets

# Aplicación básica de Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Necesario para la protección CSRF

# Definir formulario con protección CSRF
class NameForm(FlaskForm):
    name = StringField('Tu Nombre', validators=[DataRequired()])
    submit = SubmitField('Enviar')

# Ruta para mostrar y manejar el formulario
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        flash(f"¡Hola, {form.name.data}!", "success")
        return redirect('/')
    return render_template_string('''
        <!doctype html>
        <title>Ejemplo de CSRF</title>
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% for category, message in messages %}
            <div style="color:green">{{ message }}</div>
          {% endfor %}
        {% endwith %}
        <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.name.label }} {{ form.name(size=20) }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=True)
