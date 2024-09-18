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


  