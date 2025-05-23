from django.db import models

from core.models import categoria, editora

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(categoria.Categoria, on_delete=models.PROTECT, null=True, blank=True)
    editora = models.ForeignKey(editora.Editora, on_delete=models.PROTECT, null=True, blank=True)
    autor = models.ForeignKey('core.Autor', on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.quantidade})"