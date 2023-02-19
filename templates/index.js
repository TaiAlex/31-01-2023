function previewFile() {
    const preview = document.querySelector('audio');
    //const preview = document.querySelector('img');
    const file = document.querySelector('input[type=file]').files[0];
    const reader = new FileReader();
    reader.addEventListener("load", function() {
        preview.src = reader.result; // show image in <img> tag
        uploadFile(file)
    }, false);
    if (file) {
        reader.readAsDataURL(file);
    }
}

function uploadFile(file) {
    var formData = new FormData();
    formData.append('file', file);
    fetch('/upload', {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            console.log(response);
            alert("Successfuly uploaded your audio!!!");
            let btn = document.createElement("button");
            btn.innerHTML = "Dịch";
            btn.addEventListener("click", function () {
                fetch('/to_text', {
                    method: 'GET',
                })
                .then(data => {
                    console.log(data);
                    document.getElementById("text").innerHTML = response;
                });
            });
            document.body.appendChild(btn);
        })
        .catch(error => {
            console.error(error);
        });
}