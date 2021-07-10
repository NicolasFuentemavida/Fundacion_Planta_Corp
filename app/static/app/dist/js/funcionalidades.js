function confirmarDelete(id) {
    Swal.fire({
    title: 'Esta seguro que desea eliminar?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Borrar!'
        
    }).then((result) => {
        if (result.isConfirmed) {
            icon: 'success',
            Swal.fire(
                'Borrado!',
                'Borrado Correctamente.',
                'success'
            ).then(function (){
                window.location.href = "/eliminar_producto/"+id+"/";

            })
        }
    })
}