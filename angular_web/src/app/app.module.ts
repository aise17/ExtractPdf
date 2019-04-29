import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';



import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import {FormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

 import { MaterialModule } from './materials';
import { ExplicacionesComponent } from './explicaciones/explicaciones.component';
import { MenuComponent } from './menu/menu.component';
import { IrOcrComponent } from './ir-ocr/ir-ocr.component';
import { FormOcrComponent } from './from-ocr/from-ocr.component';
import { UsuarioDetalleComponent } from './usuario-detalle/usuario-detalle.component';
import { GestionDocumentosComponent } from './gestion-documentos/gestion-documentos.component';
import { MAT_DIALOG_DEFAULT_OPTIONS } from '@angular/material/dialog';
import { DialogLoginComponent } from './dialog-login/dialog-login.component';
import { ContactoComponent } from './contacto/contacto.component';
import { QuienSomosComponent } from './quien-somos/quien-somos.component';


@NgModule({
  declarations: [
    AppComponent,
    ExplicacionesComponent,
    MenuComponent,
    IrOcrComponent,
    FormOcrComponent,
    UsuarioDetalleComponent,
    GestionDocumentosComponent,
    DialogLoginComponent,
    ContactoComponent,
    QuienSomosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
    HttpClientModule,
  ],
  entryComponents: [ DialogLoginComponent ],
  providers: [
    {provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: true}}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
