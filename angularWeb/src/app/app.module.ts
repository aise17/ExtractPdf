import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ContactoComponent } from './contacto/contacto.component';
import { DialogLoginComponent } from './dialog-login/dialog-login.component';
import { ContenidoComponent } from './contenido/contenido.component';
import { GestionDocumentosComponent } from './gestion-documentos/gestion-documentos.component';
import { IrOcrComponent } from './ir-ocr/ir-ocr.component';
import { MenuComponent } from './menu/menu.component';
import { QuienSomosComponent } from './quien-somos/quien-somos.component';
import { UsuarioDetalleComponent } from './usuario-detalle/usuario-detalle.component';
import { BonosComponent } from './bonos/bonos.component';

// dependencias de angular materials
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { MaterialModule } from './materials';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { MAT_DIALOG_DEFAULT_OPTIONS } from '@angular/material/dialog';
import { FormOcrComponent } from './form-ocr/form-ocr.component';

@NgModule({
  declarations: [
    AppComponent,
    ContactoComponent,
    DialogLoginComponent,
    ContenidoComponent,
    GestionDocumentosComponent,
    IrOcrComponent,
    MenuComponent,
    QuienSomosComponent,
    UsuarioDetalleComponent,
    BonosComponent,
    FormOcrComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,    
    MaterialModule,
    FormsModule,
    HttpClientModule
  ],
  entryComponents: [ DialogLoginComponent ],
  providers: [    
    {provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: true}}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
