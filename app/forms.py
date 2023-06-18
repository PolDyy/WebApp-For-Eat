from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    pr_type = HiddenField(validators=[DataRequired()], render_kw={"id": "pr_type"})
    pr_name = HiddenField(validators=[DataRequired()], render_kw={"id": "pr_name"})
    pr_size = HiddenField(validators=[DataRequired()], render_kw={"id": "pr_size"})
    pr_cost = HiddenField(validators=[DataRequired()], render_kw={"id": "pr_cost"})
    onion = BooleanField(description="Лук", render_kw={"class": "removes-checkbox"}, default=False)
    peper = BooleanField(description="Перец", render_kw={"class": "removes-checkbox"}, default=False)
    free = BooleanField(description="Картофель фри", render_kw={"class": "addones-checkbox"}, default=False)
    meat = BooleanField(description="Мясо", render_kw={"class": "addones-checkbox"}, default=False)
    cabbage = BooleanField(description="Капуста", render_kw={"class": "addones-checkbox"}, default=False)
    carrot = BooleanField(description="Морковь", render_kw={"class": "addones-checkbox"}, default=False)

    def get_dict(self):
        data_to_return = {
            "type": self.pr_type.data,
            "name": self.pr_name.data,
            "size": self.pr_size.data,
            "cost": self.pr_cost.data,
            "additive": [item.description for item in self._get_additive() if item.data],
            "exceptions": [item.description for item in self._get_exceptions() if item.data],
            "quantity": 1,
        }
        return data_to_return

    def _get_additive(self):
        return [self.free, self.meat, self.cabbage, self.carrot]

    def _get_exceptions(self):
        return [self.onion, self.peper]

    # def get_dict(self, form):
    #     data_to_return = {
    #         "type": form.pr_type.data,
    #         "name": form.pr_name.data,
    #         "size": form.pr_size.data,
    #         "cost": form.pr_cost.data,
    #         "additive": [item.description() for item in self._get_additive(form) if item.data],
    #         "exceptions": [item.description() for item in self._get_exceptions(form) if item.data]
    #     }
    #     return data_to_return
    #
    # @staticmethod
    # def _get_additive(form):
    #     return [form.free, form.meat, form.cabbage, form.carrot]
    #
    # @staticmethod
    # def _get_exceptions(form):
    #     return [form.onion, form.peper]