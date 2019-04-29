import {MatButtonModule, MatCheckboxModule, MatDialogModule} from '@angular/material';
import { NgModule } from '@angular/core';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatIconModule} from '@angular/material/icon';

import {MatSidenavModule} from '@angular/material/sidenav';

import {MatCardModule} from '@angular/material/card';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatListModule} from '@angular/material/list';
import {MatMenuModule} from '@angular/material/menu';
import {MatFormFieldModule} from '@angular/material/form-field';

import {MatSelectModule} from '@angular/material/select';
import {MatInputModule} from '@angular/material';
import { ReactiveFormsModule } from '@angular/forms';
import {MatProgressBarModule} from '@angular/material/progress-bar';
import {ChartsModule} from 'ng2-charts';
import {MatTableModule} from '@angular/material/table';
import {MatPaginatorModule} from '@angular/material/paginator';







@NgModule({
  imports: [MatButtonModule, MatCheckboxModule, MatToolbarModule, MatIconModule,
     MatSidenavModule, MatCardModule, MatGridListModule, MatListModule, MatMenuModule,
     MatFormFieldModule, MatSelectModule, MatInputModule, ReactiveFormsModule, MatProgressBarModule,
     MatDialogModule, ChartsModule, MatTableModule, MatPaginatorModule],
  exports: [MatButtonModule, MatCheckboxModule, MatToolbarModule, MatIconModule,
     MatSidenavModule, MatCardModule, MatGridListModule, MatListModule, MatMenuModule,
     MatFormFieldModule, MatSelectModule, MatInputModule, ReactiveFormsModule, MatProgressBarModule,
     MatDialogModule, ChartsModule, MatTableModule, MatPaginatorModule],
})
export class MaterialModule { }
