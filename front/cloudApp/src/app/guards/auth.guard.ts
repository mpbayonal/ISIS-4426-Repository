import { Injectable } from '@angular/core';
import {CanActivate, Router} from '@angular/router'
import { Observable } from 'rxjs';
import {UsuarioService} from '../servicios/usuario/usuario.service'
@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private usuarioService: UsuarioService, private router: Router){}

  canActivate(){
    console.log(this.usuarioService.getToken())
    if(this.usuarioService.getToken()!=null){
  
      return true
    }
    else{
      this.router.navigate(['signin'])
      return false
    }
  }
  
}
