import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionDocumentosComponent } from './gestion-documentos.component';

describe('GestionDocumentosComponent', () => {
  let component: GestionDocumentosComponent;
  let fixture: ComponentFixture<GestionDocumentosComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GestionDocumentosComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GestionDocumentosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
