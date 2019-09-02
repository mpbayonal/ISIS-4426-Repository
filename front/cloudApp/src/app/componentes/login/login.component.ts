import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import { Router } from '@angular/router';
import {Location} from '@angular/common'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {


  constructor(private usuarioService: UsuarioService, private router:Router, private location: Location) { }

  usuario  = {
    username: "",
    email: "",
    password: ""
  }
  createUsuario ={
    username: "",
    email: "",
    password1: "",
    password2: ""

  }

  login(){
    this.usuarioService.loginUsuario(this.usuario).subscribe(
      data=>{
        
        let token = data
        this.usuarioService.setToken(token)
        this.router.navigate(['empresa/proyectos']);
        location.reload();
      }, err => console.log(err)
    )
  }

  
  signup(){
    this.usuarioService.signUpUsuario(this.createUsuario).subscribe(
      res=>{
        console.log(res)
      }, err => console.log(err)
    )
  }
  ngOnInit() {

  }

}
