import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import {Router} from '@angular/router'

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  createUsuario ={
    username: "",
    email: "",
    password1: "",
    password2: ""

  }

  
  
  constructor(private usuarioService: UsuarioService, private router: Router) {
   
  }

  signup(){
    this.usuarioService.signUpUsuario(this.createUsuario).subscribe(
      res=>{
        this.router.navigate(['signin']);
      }, err => {
        this.router.navigate(['signin']);
      }
    )
  }
  

  ngOnInit() {

  }

}


