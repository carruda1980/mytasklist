// Cria uma nova tarefa
$('#inserir').click(function() {
    var url = "/create/";
    var titulo = $("#titulo").val();
    var descricao = $("#descricao").val();
    if(titulo=="" || descricao==""){
        alert("Os campos titulo e descrição são obrigatórios, favor preenche-los!");
    }else{
        $.ajax({
            url: url,
            type: "POST",
            dataType: "text json",
            data: {
                'titulo': titulo,
                'descricao': descricao,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data){
                if(data.sucesso == 1){
                    $('#novaTarefa').modal('hide');
                    alert("Registro inserido com sucesso!");
                }else{
                    $('#novaTarefa').modal('hide');
                    alert("A tarefa não pode ser inserida, favor entrar em contato com o Suporte!");
                }
            }
        });
    }
});
// Remove uma tarefa da lista
$('#remover').click(function() {
    var url = "/delete/";
    var tarefa_id = $(this).attr('rel');
    $.ajax({
        url: url,
        type: "POST",
        dataType: "text json",
        data: {
            'tarefa_id': tarefa_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            if(data.sucesso == 1){
                alert("Registro removido com sucesso!");
            }else{
                alert("A tarefa não pode ser removida, favor entrar em contato com o Suporte!");
            }
        }
    });
});
// Exibe uma tarefa da lista no modal
$('#linkeditar').click(function() {
    var url = "/getedit/";
    var tarefa_id = $(this).attr('rel');
    $.ajax({
        url: url,
        type: "GET",
        dataType: "text json",
        data: {
            'tarefa_id': tarefa_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            if(data.sucesso==1){
                $("#edittitulo").val(data.titulo);
                $("#editdescricao").val(data.descricao);
                $("#edittarefaid").val(data.id);
                $('#editarTarefa').modal('show');
            }
        }
    });
});
// Edita uma tarefa da lista
$('#editar').click(function() {
    var url = "/edit/";
    var edittarefaid = $("#edittarefaid").val();
    var edittitulo = $("#edittitulo").val();
    var editdescricao = $("#editdescricao").val();
    $.ajax({
        url: url,
        type: "POST",
        dataType: "text json",
        data: {
            'edittarefaid': edittarefaid,
            'edittitulo': edittitulo,
            'editdescricao': editdescricao,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            if(data.sucesso==1){
                alert("Registro editado com sucesso!");
                $('#editarTarefa').modal('hide');
            }else{
                $('#editarTarefa').modal('hide');
                alert("A tarefa não pode ser atualizada, favor entrar em contato com o Suporte!");
            }
        }
    });
});