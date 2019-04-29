import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ExplicacionesComponent } from './explicaciones/explicaciones.component';
import { FormOcrComponent } from './from-ocr/from-ocr.component';
import { UsuarioDetalleComponent } from './usuario-detalle/usuario-detalle.component';
import { GestionDocumentosComponent } from './gestion-documentos/gestion-documentos.component';
import { ContactoComponent } from './contacto/contacto.component';
import { QuienSomosComponent } from './quien-somos/quien-somos.component';

const routes: Routes = [
  {path: '', redirectTo: '/index', pathMatch: 'full' },
  {path: 'ocr', component: FormOcrComponent },
  {path: 'index', component: ExplicacionesComponent },
  {path: 'usuario', component: UsuarioDetalleComponent },
  {path: 'gestio-archivos', component: GestionDocumentosComponent },
  {path: 'contacto', component: ContactoComponent},
  {path: 'quienSomos', component: QuienSomosComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
