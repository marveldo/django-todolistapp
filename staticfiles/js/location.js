let changes = document.getElementsByClassName('urlchange')

  
for(let change in changes){
 changes[change].addEventListener('click', e=>{
   
   url = e.target.dataset.href
   window.location = url
 })
}