import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OcrContenidoComponent } from './ocr-contenido.component';

describe('OcrContenidoComponent', () => {
  let component: OcrContenidoComponent;
  let fixture: ComponentFixture<OcrContenidoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OcrContenidoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OcrContenidoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
