import { Component, OnInit } from '@angular/core';
import { DiseñoService } from 'src/app/servicios/diseño/diseño.service';
import {Router, ActivatedRoute} from '@angular/router';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import { DomSanitizer } from '@angular/platform-browser';



@Component({
  selector: 'app-ver-diseno',
  templateUrl: './ver-diseno.component.html',
  styleUrls: ['./ver-diseno.component.css']
})
export class VerDisenoComponent implements OnInit {

  public isLogged= false;
  diseno: any;
  constructor(private disenoService: DiseñoService,private activated : ActivatedRoute, private usuarioService: UsuarioService,
    public sanitizer:DomSanitizer) { }

  chequearLogin(){
    if(this.usuarioService.getToken()){
      this.isLogged=true;
    }else{
      this.isLogged=false;
    }
  }
  ngOnInit() {

    this.chequearLogin();
    this.disenoService.getDisenoId(this.activated.snapshot.params.idDiseño).subscribe(
      res=>{
        this.diseno= res;
      }, err => console.log(err)
    )

   
    
  }
  imagenes(img){
    this.sanitizer.bypassSecurityTrustResourceUrl(img)
  }

}
