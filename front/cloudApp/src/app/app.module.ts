import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import {MatPaginatorModule} from '@angular/material/paginator';


import { AppComponent } from './app.component';
import { LoginComponent } from './componentes/login/login.component';
import { HomeComponent } from './componentes/home/home.component';
import { NavegacionComponent } from './componentes/navegacion/navegacion.component';
import { SignupComponent } from './componentes/signup/signup.component';
import { ListarProyectosComponent } from './componentes/proyectos/listar-proyectos/listar-proyectos.component';
import { EditarProyectosComponent } from './componentes/proyectos/editar-proyectos/editar-proyectos.component';
import { VerProyectosComponent } from './componentes/proyectos/ver-proyectos/ver-proyectos.component';
import { ListarDisenosComponent } from './componentes/diseños/listar-disenos/listar-disenos.component';
import { AgregarProyectoComponent } from './componentes/proyectos/agregar-proyecto/agregar-proyecto.component';
import { AgregarDisenoComponent } from './componentes/diseños/agregar-diseno/agregar-diseno.component';
import { ConfirmarEnvioComponent } from './componentes/diseños/confirmar-envio/confirmar-envio.component';
import {ProyectoService} from './servicios/proyecto/proyecto.service';
import {HttpClientModule} from '@angular/common/http';
import { PaginatePipe } from './pipes/paginate.pipe';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    NavegacionComponent,
    SignupComponent,
    ListarProyectosComponent,
    EditarProyectosComponent,
    VerProyectosComponent,
    ListarDisenosComponent,
    AgregarProyectoComponent,
    AgregarDisenoComponent,
    ConfirmarEnvioComponent,
    PaginatePipe
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatPaginatorModule,
    BrowserAnimationsModule
  ],
  providers: [ProyectoService],
  bootstrap: [AppComponent]
})

export class AppModule { }
