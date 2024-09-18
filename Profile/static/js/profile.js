const defaultFile = 'https://via.placeholder.com/150';

const file = document.getElementById( 'profile-img-preview' );
const img = document.getElementById( 'profile-avatar' );
file.addEventListener( 'change', e => {
  if( e.target.files[0] ){
    const reader = new FileReader( );
    reader.onload = function( e ){
      img.src = e.target.result;
    }
    reader.readAsDataURL(e.target.files[0])
  }else{
    img.src = defaultFile;
  }
} );

const selectImage = document.getElementById('select-image');
const inpuFile = document.querySelector(#file);
selectImage.addEventListener('click',function(){
  inpuFile.click();
})
inputFile.addEventListener('change',function(){
  const image = this.files[0]
  console.log(image);
  const reader = new FileReader();
  reader.onload=()=>{
    const imgUrl = reader.result;
    const img = document.createElement('img');
    img.src = imgUrl;
  }
  reader.readAsDataURL(image);
})
  