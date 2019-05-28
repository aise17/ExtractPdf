import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IrScrapyComponent } from './ir-scrapy.component';

describe('IrScrapyComponent', () => {
  let component: IrScrapyComponent;
  let fixture: ComponentFixture<IrScrapyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IrScrapyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IrScrapyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
