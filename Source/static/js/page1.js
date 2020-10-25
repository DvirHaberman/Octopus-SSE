// const mybutton = document.querySelector(".mybutton");

// mybutton.addEventListener('click', () => alert('a button has been pressed!'));

$(document).ready(() => {
    data_table = $('#data_table').DataTable({
        ajax: "/get_data",
        columns: [
            { title: "NAME", "data": "names" },
            { title: "TOWN", "data": "towns" },
            { title: "HOBBY", "data": "hobbies" }
        ]
    });


});

// data.ajax.reload();