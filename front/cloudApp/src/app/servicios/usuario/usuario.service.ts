import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  API_URI = 'http://54.175.1.161/api';
  constructor(private http: HttpClient, private router: Router) { }

  getUrl(username){
    return this.http.get(`${this.API_URI}/user/${username}/`)
  }

  loginUsuario(usuario){
    return this.http.post(`${this.API_URI}/auth/login/`, usuario );
  }

  signUpUsuario(usuario){
    return this.http.post(`${this.API_URI}/auth/signup/`, usuario );
  }

  setToken(token): void {
    localStorage.setItem("accessToken", token);
  }
  
  getToken() {
    return localStorage.getItem("accessToken");
  }
  logoutUser() {
    localStorage.removeItem("accessToken");
    localStorage.removeItem("usuario");
    localStorage.removeItem("url");
    localStorage.removeItem("id");
    this.router.navigate(['/']);
  }
}
