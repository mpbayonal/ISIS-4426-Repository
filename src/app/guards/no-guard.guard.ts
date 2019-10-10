import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { UsuarioService } from '../servicios/usuario/usuario.service';

@Injectable({
  providedIn: 'root'
})
export class NoGuardGuard implements CanActivate {
  constructor(private usuarioService: UsuarioService, private router: Router) { }
  canActivate() {

    if (this.usuarioService.getToken() == null) {

      return true;
    } else {
      console.log(localStorage.getItem('url'));
      this.router.navigate(['empresa/' + localStorage.getItem('url') + '/proyectos']);
      return false;
    }
  }

}
