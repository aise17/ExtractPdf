import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Injectable } from '@angular/core';

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
import { DialogErrorComponent } from './dialog-error/dialog-error.component';
import { FaqsComponent } from './faqs/faqs.component';
import { HeatmapComponent } from './heatmap/heatmap.component';

import { AgmCoreModule } from '@agm/core';
import { from } from 'rxjs';
import { AdminComponent } from './admin/admin.component';
import { CompraBonosEstadisticaAdminComponent } from './compra-bonos-estadistica-admin/compra-bonos-estadistica-admin.component';
import { GestionBonosComponent } from './gestion-bonos/gestion-bonos.component';
import { FormScrapyComponent } from './form-scrapy/form-scrapy.component';
import { OcrContenidoComponent } from './ocr-contenido/ocr-contenido.component';
import { ScrapyContenidoComponent } from './scrapy-contenido/scrapy-contenido.component';
import { IrScrapyComponent } from './ir-scrapy/ir-scrapy.component';
import { RequestByYearEstadisticaAdminComponent } from './request-by-year-estadistica-admin/request-by-year-estadistica-admin.component';
import { MarcoFormOcrComponent } from './marco-form-ocr/marco-form-ocr.component';
import { MarcoFormScrapyComponent } from './marco-form-scrapy/marco-form-scrapy.component';
import { NormasOcrComponent } from './normas-ocr/normas-ocr.component';
import { NormasScrapyComponent } from './normas-scrapy/normas-scrapy.component';
import { GestionCampaingsComponent } from './gestion-campaings/gestion-campaings.component';




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
    FormOcrComponent,
    DialogErrorComponent,
    FaqsComponent,
    HeatmapComponent,
    AdminComponent,
    CompraBonosEstadisticaAdminComponent,
    GestionBonosComponent,
    FormScrapyComponent,
    OcrContenidoComponent,
    ScrapyContenidoComponent,
    IrScrapyComponent,
    RequestByYearEstadisticaAdminComponent,
    MarcoFormOcrComponent,
    MarcoFormScrapyComponent,
    NormasOcrComponent,
    NormasScrapyComponent,
    GestionCampaingsComponent,
    

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,    
    MaterialModule,
    FormsModule,
    HttpClientModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyB2nZL8uAHgxjQ78tU9gBCgi5NxTD2bmjk'
    })
    
  ],
  entryComponents: [ DialogLoginComponent, DialogErrorComponent ],
  providers: [    
    {provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: true}}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

