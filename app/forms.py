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
            "cost": int(self.pr_cost.data),
            "info": self._get_info_field(),
            "quantity": 1,
        }
        return data_to_return

    def _get_additive_desc(self):
        additive = [self.free, self.meat, self.cabbage, self.carrot]
        return [item.description for item in additive if item.data]

    def _get_exceptions_desc(self):
        exceptions = [self.onion, self.peper]
        return [item.description for item in exceptions if item.data]

    def _get_additive(self):
        additive = self._get_additive_desc()
        if len(additive) != 0:
            if len(additive) == 1:
                return f"Добавить: {additive[0]}"
            sting_start = "Добавить: "
            string_end = ""
            for elem in additive:
                string_end = "; ".join((elem, string_end))

            return "".join((sting_start, string_end))

    def _get_exceptions(self):
        exceptions = self._get_exceptions_desc()
        if len(exceptions) != 0:
            if len(exceptions) == 1:
                return f"Убрать: {exceptions[0]}"
            sting_start = "Убрать: "
            string_end = ""
            for elem in exceptions:
                string_end = "; ".join((elem, string_end))

            return "".join((sting_start, string_end))

    def _get_info_field(self):
        additive = self._get_additive()
        exceptions = self._get_exceptions()
        if not additive and not exceptions:
            return "Без изменений"
        if additive and exceptions:
            return f"{additive}\n{exceptions}"
        elif additive:
            return additive
        else:
            return exceptions
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