let deletebuttons = document.getElementsByClassName('delete')
  
 
for (let deletebutton in deletebuttons ){
  deletebuttons[deletebutton].addEventListener('click', (e)=>{
   
   let taskid = e.target.dataset.id
    let action = e.target.dataset.action
    console.log(taskid,action)
   let csrftoken = getCookie('csrftoken')
    url ='/delete/'
    options = {
      method : 'POST',
      headers : {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body : JSON.stringify({'id': taskid,'action': action})
    }
    fetch(url,options).then(response => response.json()).then(data => console.log(data))
   location.reload()

   
  })
}