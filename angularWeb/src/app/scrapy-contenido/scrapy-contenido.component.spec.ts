import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScrapyContenidoComponent } from './scrapy-contenido.component';

describe('ScrapyContenidoComponent', () => {
  let component: ScrapyContenidoComponent;
  let fixture: ComponentFixture<ScrapyContenidoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScrapyContenidoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScrapyContenidoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
