Forms
=====

Like django-localflavors the CPFField and CNPJField are validators to Brazilian CPF and CNPJ with a big difference, It removes repeated sequences and undue values.

Usage:

Your Just need to add your form class. Example using ModelForm:


.. code-block:: python

    from django_stuff.forms import CPFField, CNPJField

    ...

    class TestForm(forms.ModelForm):
        class Meta:
            model = YourModel

        fields = [..., 'cpf', 'cnpj']
        widgets = {
            'cpf': CNPJField(),
            'cnpj': CNPJField(),
        }





