import { Component, OnInit } from '@angular/core';
import { UsuarioService } from 'src/app/servicios/usuario/usuario.service';
import { Router } from '@angular/router';
import { FlashMessagesService } from 'angular2-flash-messages';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  createUsuario = {
    username: '',
    email: '',
    password1: '',
    password2: ''

  };



  constructor(
    private usuarioService: UsuarioService,
    private router: Router,
    private flashMessagesService: FlashMessagesService) {

  }

  signup() {
    this.usuarioService.signUpUsuario(this.createUsuario).subscribe(
      res => {
        this.router.navigate(['signin']);
      }, err => {

        if (err.status === 500) {

          this.router.navigate(['signin']);
          this.flashMessagesService.show('Registro exitoso', { cssClass: 'alert-success', timeout: 6000 });
        } else if (err.satus !== 500) {

          if (this.createUsuario.password1 !== this.createUsuario.password2) {
            this.flashMessagesService.show('Las contraseñas no coinciden, intentalo otra vez', { cssClass: 'alert-danger', timeout: 6000 });
          } else {
            this.flashMessagesService.show('Error a registrarse intentalo otra vez', { cssClass: 'alert-danger', timeout: 6000 });
          }

          this.router.navigate(['signup']);
        }

      }
    );
  }


  ngOnInit() {

  }

}


