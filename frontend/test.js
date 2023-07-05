
const gettask = () => {
    fetch('http://127.0.0.1:8000/api/Tasks/')
    .then(response => response.json())
    .then(data => console.log(data))
}
gettask()