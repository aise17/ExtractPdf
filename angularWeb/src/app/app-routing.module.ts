import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FormOcrComponent } from './form-ocr/form-ocr.component';
import { ContenidoComponent } from './contenido/contenido.component';
import { UsuarioDetalleComponent } from './usuario-detalle/usuario-detalle.component';
import { QuienSomosComponent } from './quien-somos/quien-somos.component';
import { ContactoComponent } from './contacto/contacto.component';
import { GestionDocumentosComponent } from './gestion-documentos/gestion-documentos.component';
import { BonosComponent } from './bonos/bonos.component';
import { FaqsComponent } from './faqs/faqs.component';
import { HeatmapComponent } from './heatmap/heatmap.component';
import { AdminComponent } from './admin/admin.component';
import { GestionBonosComponent } from './gestion-bonos/gestion-bonos.component';
import { FormScrapyComponent } from './form-scrapy/form-scrapy.component';
import { MarcoFormOcrComponent } from './marco-form-ocr/marco-form-ocr.component';
import { MarcoFormScrapyComponent } from './marco-form-scrapy/marco-form-scrapy.component';

const routes: Routes = [
  {path: '', redirectTo: '/index', pathMatch: 'full' },
  {path: 'ocr', component: MarcoFormOcrComponent },
  {path: 'index', component: ContenidoComponent },
  {path: 'usuario', component: UsuarioDetalleComponent },
  {path: 'gestio-archivos', component: GestionDocumentosComponent },
  {path: 'contacto', component: ContactoComponent},
  {path: 'quienSomos', component: QuienSomosComponent},
  {path: 'bonos', component: BonosComponent},
  {path: 'faqs', component: FaqsComponent},
  {path: 'admin', component: AdminComponent},
  {path: 'map', component: HeatmapComponent},
  {path: 'gest-bon', component: GestionBonosComponent},
  {path: 'scrapy', component: MarcoFormScrapyComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
