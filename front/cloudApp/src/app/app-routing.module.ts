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

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    pathMatch: 'full'
  },
  {
    path: 'signin',
    component: LoginComponent,
  },
  {
    path: 'signup',
    component: SignupComponent
  },
  {
    path:'empresa/proyectos',
    component: ListarProyectosComponent
  },
  {
    path:'empresa/proyectos/idProyecto/diseños',
    component: ListarDisenosComponent
  },{
    path: 'empresa/proyectos/idProyecto/editar',
    component: EditarProyectosComponent
  },
  {
    path: 'empresa/proyectos/agregar',
    component: AgregarProyectoComponent
  },
  {
    path: 'empresa/proyectos/idProyecto/diseños/agregarDiseño',
    component: AgregarDisenoComponent
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
