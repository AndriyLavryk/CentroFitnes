from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, NumberRange

class ClientForm(FlaskForm):
    id = HiddenField('id')  # Скрытое поле для идентификатора клиента
    first_name = StringField('Имя', validators=[DataRequired()])  # Поле для имени клиента
    last_name = StringField('Фамилия', validators=[DataRequired()])  # Поле для фамилии клиента
    membership = IntegerField('Членство',
                              validators=[DataRequired(),
                                          NumberRange(min=1, message="Должно быть положительным числом")])  # Поле для номера членства
    save = SubmitField('Сохранить')  # Кнопка для отправки формы
