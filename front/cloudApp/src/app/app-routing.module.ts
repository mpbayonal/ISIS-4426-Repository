import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {HomeComponent} from './componentes/home/home.component';
import {LoginComponent} from './componentes/login/login.component';
import {SignupComponent} from './componentes/signup/signup.component';
import {ListarProyectosComponent} from './componentes/proyectos/listar-proyectos/listar-proyectos.component';
import {ListarDisenosComponent} from './componentes/diseños/listar-disenos/listar-disenos.component';
import {AgregarProyectoComponent} from './componentes/proyectos/agregar-proyecto/agregar-proyecto.component';
import {EditarProyectosComponent} from './componentes/proyectos/editar-proyectos/editar-proyectos.component';
import {AgregarDisenoComponent} from './componentes/diseños/agregar-diseno/agregar-diseno.component';
import {ConfirmarEnvioComponent} from './componentes/diseños/confirmar-envio/confirmar-envio.component';
import {VerDisenoComponent} from './componentes/diseños/ver-diseno/ver-diseno.component';
import { AuthGuard } from './guards/auth.guard';
import {NoGuardGuard} from './guards/no-guard.guard';


const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    pathMatch: 'full'
  },
  {
    path: 'signin',
    component: LoginComponent,
    canActivate: [NoGuardGuard]
  },
  {
    path: 'signup',
    component: SignupComponent,
    canActivate: [NoGuardGuard]
  },
  {
    path:'empresa/:url/proyectos',
    component: ListarProyectosComponent
  },
  {
    path:'empresa/proyectos/:idProyecto/disenos',
    component: ListarDisenosComponent
  },
  {
    path: 'empresa/proyectos/:idProyecto/editar',
    component: EditarProyectosComponent,
    canActivate: [AuthGuard]
  },
  {
    
    path: 'empresa/:url/proyectos/agregar',
    component: AgregarProyectoComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'empresa/proyectos/:idProyecto/disenos/agregarDiseno',
    component: AgregarDisenoComponent
  },
  {
    path: 'empresa/proyectos/diseños/:idDiseño',
    component: VerDisenoComponent
  },
  {
    path: 'empresa/proyecto/idProyecto/diseños/agregarDiseño/mensaje',
    component:ConfirmarEnvioComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
