from django import template

register = template.Library()

@register.filter
def add_class(field, css_classes):
    if hasattr(field, 'field'):  # Verifica se field é um campo de formulário
        widget = field.field.widget
        existing_classes = widget.attrs.get('class', '').split(' ')
        new_classes = css_classes.split(' ')
        final_classes = existing_classes + [c for c in new_classes if c not in existing_classes]
        widget.attrs['class'] = ' '.join(final_classes)
    return field
