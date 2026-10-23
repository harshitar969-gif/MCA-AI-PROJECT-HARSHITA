document.getElementById('studentForm').addEventListener('submit', function(e){
    e.preventDefault();

    let name = document.getElementById('name').value;
    let att = parseInt(document.getElementById('attendance').value);
    let assign = parseInt(document.getElementById('assignment').value);
    let internal = parseInt(document.getElementById('internal').value);
    let study = parseInt(document.getElementById('study').value);

    // Simple AI Logic (MCA Level)
    let total = (att * 0.4) + (assign/20*100 * 0.2) + (internal/30*100 * 0.3) + (study*10 * 0.1);
    let result = total >= 50 ? "Pass" : "Fail";

    // Result dikhao
    document.getElementById('resultBox').classList.remove('hidden');
    document.getElementById('resultText').innerHTML = 
        `Student: ${name} <br> Result: <span class="${result.toLowerCase()}">${result}</span>`;
    document.getElementById('perText').innerText = `Predicted: ${total.toFixed(1)}%`;
});