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
                console.log(data);
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