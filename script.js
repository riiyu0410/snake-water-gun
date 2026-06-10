function playGame(choice){

    fetch(`/play/${choice}`)
    .then(response => response.json())
    .then(data => {

        document.getElementById("result").innerText =
            data.result;

        document.getElementById("choices").innerText =
            `You: ${data.player} | Computer: ${data.computer}`;
    });
}